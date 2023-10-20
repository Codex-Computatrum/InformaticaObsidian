package org.example;

class B extends A {
    public String f(A x, int y, float z){
        return "B1" + f(this, (int) z, z);
    }
    public String f(A x, long y, long z){ return "B2";}
    public String f(B x, int y, int z){ return "B3";}
}

