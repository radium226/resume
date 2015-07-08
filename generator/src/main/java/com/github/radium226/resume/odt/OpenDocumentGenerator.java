package com.github.radium226.resume.odt;

import com.github.radium226.io.Resources;
import com.github.radium226.resume.GenerationException;
import com.github.radium226.resume.Generator;
import com.github.radium226.xml.Canonicalizer;
import com.github.radium226.xml.IncludeResolver;
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
import java.io.FileOutputStream;
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
    
    public File extractFilesToTempFolder() throws IOException {
        File tempFolder = Files.createTempDirectory("resume-odf").toFile();
        Resources.copyResources("generators/odf", tempFolder);
        return tempFolder;
    }

    public void generate(File inputFile, OutputStream outputStream) throws TransformerException, IOException {
        File tempFolder = extractFilesToTempFolder();
        
        Document inputDocument = parse(inputFile);
        
        File workingFolder = inputFile.getParentFile();
        new IncludeResolver(workingFolder).resolveIncludes(inputDocument);
        new Canonicalizer().canonicalize(inputDocument);
        System.out.println("tempFolder=" + tempFolder);
        Document contentDocument = transform(inputDocument).relativeTo(tempFolder).with(new File(tempFolder, "main.xslt"));
        print(contentDocument).to(new File(new File(tempFolder, "template"), "content.xml"));
        assemble(new File(tempFolder, "template"), outputStream);
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
    public void generate(File inputFile, File outputFile) throws GenerationException {
        try {
            generate(inputFile, new FileOutputStream(outputFile));
        } catch (IOException | TransformerException e) {
            throw new GenerationException(e);
        }
    }

    @Override
    public String defaultFileNameExtension() {
        return DEFAULT_FILE_NAME_EXTENSION;
    }

}
