package fun.mrctf.springcoffee.controller;

import com.esotericsoftware.kryo.Kryo;

public class BaseController {
    protected Kryo kryo = new Kryo();
}
