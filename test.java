import java.util.Scanner
class exploding_cat{
   public static void main(String[] args){
        Scanner scanthing = new Scanner(System.in);
        System.out.println("hello! what is your name?");
        String name=scanthing.next();
        execewt something=new execewt(name);
        something.main();
        something.other();
   }
}
class execewt{
    String name;
    public void main(){
        System.out.printf("%s","hi "+name+"!");
    }
    public void other(){
        System.out.printf("%s","hello "+name+"!");
    }
}