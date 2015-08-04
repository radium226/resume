package com.github.radium226.resume.odt;

import com.github.radium226.Colors;
import com.github.radium226.io.Resources;
import com.github.radium226.resume.GenerationException;
import com.github.radium226.resume.Generator;
import com.github.radium226.xml.Canonicalizer;
import com.github.radium226.xml.IncludeResolver;
import com.github.radium226.xml.Style;
import com.github.radium226.xml.XML;
import com.google.common.collect.Lists;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.Collections;
import java.util.List;
import java.util.zip.CRC32;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;
import static com.github.radium226.xml.XML.*;
import com.google.common.collect.ImmutableMap;
import java.io.FileOutputStream;
import java.util.Map;
import java.util.Optional;
import javax.xml.transform.TransformerException;
import org.w3c.dom.Document;

public class OpenDocumentGenerator implements Generator {

    public static final Path MIME_TYPE_PATH = Paths.get("mimetype");
    
    public static final String DEFAULT_FILE_NAME_EXTENSION = "odt";
    
//    public static final File TRANSFORMATION_FILE = new File("src/main/generator/odf/main.xslt");
//    public static final File TEMPLATE_FOLDER = new File("src/main/generator/odf/template");
//    public static final File CONTENT_FILE = new File(TEMPLATE_FOLDER, "content.xml");
    
    
    public OpenDocumentGenerator() {
        super();
    }
    
    public File extractFilesToTempFolder(Optional<File> optionalTempFolder) throws IOException {
        File tempFolder = optionalTempFolder.orElse(Files.createTempDirectory("resume-odf").toFile());
        Resources.copyResources("generators/odf", tempFolder);
        return tempFolder;
    }

    public void generate(File inputFile, OutputStream outputStream, String color, Optional<File> optionalTempFolder) throws TransformerException, IOException {
        File tempFolder = extractFilesToTempFolder(optionalTempFolder);
        
        ImmutableMap.Builder<String, String> variableBuilder = ImmutableMap.builder();
        int count = 3;
        List<String> colorShades = Colors.shadesOf(color, count);
        for (int i = 1; i <= count; i++) {
            String colorShade = colorShades.get(i - 1);
            variableBuilder = variableBuilder.put("color" + i, colorShade);
        }
        Map<String, String> variables = variableBuilder.build();
        
        File workingFolder = inputFile.getParentFile();
        Document document = normalize(parse(inputFile), tempFolder, workingFolder);
        System.out.println("tempFolder=" + tempFolder);
        
        generateContent(document, tempFolder, variables);
        generateStyle(document, tempFolder, variables);
        
        assemble(new File(tempFolder, "template"), outputStream);
    }
    
    public void generateContent(Document document, File tempFolder, Map<String, String> variables) throws TransformerException, IOException {
        File contentTransformationFolder = tempFolder.toPath().resolve("transformations/content").toFile();
        Document contentDocument = transform(document)
                .relativeTo(contentTransformationFolder)
                .bindAll(variables)
            .with(new File(contentTransformationFolder, "content.xslt"));
        print(contentDocument).to(new File(new File(tempFolder, "template"), "content.xml"));
    }
    
    public void generateStyle(Document document, File tempFolder, Map<String, String> variables) throws TransformerException, IOException {
        File styleTransformationFolder = tempFolder.toPath().resolve("transformations/styles").toFile();
        Document styleDocument = transform(document)
                .relativeTo(styleTransformationFolder)
                .bindAll(variables)
            .with(new File(styleTransformationFolder, "styles.xslt"));
        print(styleDocument).to(tempFolder.toPath().resolve("template/styles.xml").toFile());
    }
    
    public Document normalize(Document document, File tempFolder, File workingFolder) {
        document = new IncludeResolver(workingFolder).resolveIncludes(document);
        
        document = transform(document).with(tempFolder.toPath().resolve("transformations/normalize.xslt").toFile());
        
        document = new Canonicalizer().canonicalize(document);
        System.out.println("HEYYO! ");
        try {
            print(document).to(System.out, Style.PRETTY);
        } catch (TransformerException e) {
            e.printStackTrace(System.err);
        }
        return document;
    }

    public void assemble(File folder, OutputStream outputStream) throws IOException {
        assemble(folder.toPath(), outputStream);
    }
    
    public void assemble(Path folderPath, OutputStream outputStream) throws IOException {
        try (ZipOutputStream zipOutputStream = new ZipOutputStream(outputStream)) {
            // We list all file paths stored in the folder
            List<Path> filePaths = Lists.newArrayList();
            Files.walkFileTree(folderPath, new SimpleFileVisitor<Path>() {
                
                @Override
                public FileVisitResult visitFile(Path visitedFilePath, BasicFileAttributes attributes) throws IOException {
                    filePaths.add(visitedFilePath);
                    return FileVisitResult.CONTINUE;
                }
                
            });
            
            // We sort them in order to have the mime-type file first
            Collections.sort(filePaths, (Path oneFilePath, Path otherFilePath) -> {
                return oneFilePath.getFileName().equals(MIME_TYPE_PATH) ? -1 : 0;
            });
            
            // We archive them, but without compression for the mime-type file
            for (Path filePath : filePaths) {
                String name = folderPath.relativize(filePath).toString();
                ZipEntry zipEntry = new ZipEntry(name);
                if (filePath.getFileName().equals(MIME_TYPE_PATH)) {
                    zipEntry.setMethod(ZipEntry.STORED);
                    CRC32 crc32 = new CRC32();
                    byte[] bytes = Files.readAllBytes(filePath);
                    crc32.update(bytes);
                    zipEntry.setCrc(crc32.getValue());
                    zipEntry.setSize(bytes.length);
                    zipEntry.setCompressedSize(bytes.length);
                    zipOutputStream.putNextEntry(zipEntry);
                } else {
                    zipOutputStream.putNextEntry(zipEntry);
                }
                Files.copy(filePath, zipOutputStream);
                zipOutputStream.closeEntry();
            }
        }
    }

    @Override
    public void generate(File inputFile, File outputFile, String color, Optional<File> tempFolder) throws GenerationException {
        try {
            generate(inputFile, new FileOutputStream(outputFile), color, tempFolder);
        } catch (IOException | TransformerException e) {
            throw new GenerationException(e);
        }
    }

    @Override
    public String defaultFileNameExtension() {
        return DEFAULT_FILE_NAME_EXTENSION;
    }

}
