package fun.mrctf.springcoffee.model;

public class Mocha implements ExtraFlavor{
    double chocolate = 0.2;

    @Override
    public String getName() {
        return "Mocha";
    }
}
