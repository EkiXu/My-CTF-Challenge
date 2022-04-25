package fun.mrctf.springcoffee.controller;

import fun.mrctf.springcoffee.model.Message;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class IndexController{
    @RequestMapping("/")
    public Message index(){
        return new Message(200,"There is no flag but a cup of coffee");
    }
}
