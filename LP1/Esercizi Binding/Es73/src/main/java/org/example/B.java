package org.example;

class B extends A {
    public String f(B x, Object[] y) { return "B1−>" + f(y, y); }
}
