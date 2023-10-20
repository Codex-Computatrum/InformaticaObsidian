package org.example;

class A {
    private String f(A x, int y, float z){
        return "A1";
    }
    public String f(A x, double y, float z){ return "A2";}
    public String f(B x, float y, long z){ return "A3";}
}

