/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.github.radium226.util;

/**
 *
 * @author adrien
 */
public class ThrowableThrower {
    
    // http://www.mail-archive.com/javaposse@googlegroups.com/msg05984.html
    public static void throwThrowable(Throwable throwable) {
        if (throwable == null) {
            throw new NullPointerException();
        }
        throwThrowable0(throwable);
}

    @SuppressWarnings("unchecked")
    private static <T extends Throwable> void throwThrowable0(Throwable throwable) throws T {
        throw (T) throwable;
    }
    
}
