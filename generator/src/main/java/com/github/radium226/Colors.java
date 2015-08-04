package com.github.radium226;

import com.google.common.collect.Lists;
import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class Colors {

    public static List<String> shadesOf(String hex, int count) {
        return Lists.transform(shadesOf(hex2color(hex), count), (color) -> color2hex(color));
    }

    public static String color2hex(Color color) {
        return String.format("#%02x%02x%02x", color.getRed(), color.getGreen(), color.getBlue());
    }

    public static Color hex2color(String hex) {
        return new Color(
                Integer.valueOf(hex.substring(1, 3), 16),
                Integer.valueOf(hex.substring(3, 5), 16),
                Integer.valueOf(hex.substring(5, 7), 16));
    }

    public static List<Color> shadesOf(Color color, int count) {
        List<Color> colorBands = new ArrayList<>(count);
        for (int index = 0; index < count; index++) {
            colorBands.add(darkenColor(color, (double) index / (double) count));
        }
        return colorBands;
    }

    public static Color darkenColor(Color color, double fraction) {
        int red = (int) Math.round(Math.max(0, color.getRed() - 255 * fraction));
        int green = (int) Math.round(Math.max(0, color.getGreen() - 255 * fraction));
        int blue = (int) Math.round(Math.max(0, color.getBlue() - 255 * fraction));
        int alpha = color.getAlpha();
        return new Color(red, green, blue, alpha);
    }

}
