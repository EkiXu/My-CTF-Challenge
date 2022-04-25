package fun.mrctf.springcoffee.model;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Message {
    int code;
    String detail;
    Object data;
    public Message(int code,String detail){
        this.code = code;
        this.detail = detail;
    }
    public Message(int code,String detail,Object data){
        this.code = code;
        this.detail = detail;
        this.data = data;
    }
}
