package fun.mrctf.springcoffee.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CoffeeRequest{
    public double espresso;
    public double hotWater;
    public double milkFoam;
    public double steamMilk;
    public String extraFlavor;
}
