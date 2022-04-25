package fun.mrctf.springcoffee.controller;

import com.esotericsoftware.kryo.Kryo;
import com.esotericsoftware.kryo.io.Input;
import com.esotericsoftware.kryo.io.Output;
import fun.mrctf.springcoffee.model.CoffeeRequest;
import fun.mrctf.springcoffee.model.ExtraFlavor;
import fun.mrctf.springcoffee.model.Message;
import fun.mrctf.springcoffee.model.Mocha;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.lang.reflect.Method;
import java.util.Base64;

import java.io.ByteArrayInputStream;

@RestController
public class CoffeeController extends BaseController{
    @RequestMapping("/coffee/index")
    public Message index(){
        return new Message(200,"what do your want? please order");
    }

    @RequestMapping("/coffee/order")
    public Message order(@RequestBody CoffeeRequest coffee){
        if(coffee.extraFlavor!=null){
            ByteArrayInputStream bas = new ByteArrayInputStream(Base64.getDecoder().decode(coffee.extraFlavor));
            Input input = new Input(bas);
            ExtraFlavor flavor = (ExtraFlavor) kryo.readClassAndObject(input);
            return new Message(200, flavor.getName());
        }
        if(coffee.espresso > 0.5){
            return new Message(200,"DOPPIO");
        }else{
            if(coffee.hotWater > 0.5){
                return new Message(200,"AMERICANO");
            }else if(coffee.milkFoam > 0 && coffee.steamMilk > 0){
                if(coffee.steamMilk > coffee.milkFoam){
                    return new Message(200,"CAPPUCCINO");
                }else return new Message(200,"Latte");
            }else if(coffee.espresso > 0){
                return new Message(200,"Espresso");
            }else return new Message(200,"empty");
        }
    }

    @RequestMapping("/coffee/demo")
    public Message demoFlavor(@RequestBody String raw) throws Exception {
        System.out.println(raw);
        JSONObject serializeConfig = new JSONObject(raw);
        if(serializeConfig.has("polish")&&serializeConfig.getBoolean("polish")){
            kryo=new Kryo();
            for (Method setMethod:kryo.getClass().getDeclaredMethods()) {
                if(!setMethod.getName().startsWith("set")){
                    continue;
                }
                try {
                    Object p1 = serializeConfig.get(setMethod.getName().substring(3));
                    if(!setMethod.getParameterTypes()[0].isPrimitive()){
                        try {
                            p1 = Class.forName((String) p1).newInstance();
                            setMethod.invoke(kryo, p1);
                        }catch (Exception e){
                            e.printStackTrace();
                        }
                    }else{
                        setMethod.invoke(kryo,p1);
                    }
                }catch (Exception e){
                    continue;
                }
            }
        }

        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        Output output = new Output(bos);
        kryo.register(Mocha.class);
        kryo.writeClassAndObject(output,new Mocha());
        output.flush();
        output.close();

        return new Message(200,"Mocha!",Base64.getEncoder().encode(bos.toByteArray()));
    }
}
