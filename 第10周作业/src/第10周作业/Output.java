package 第10周作业;
import java.util.*;
public class Output implements Runnable {
	private Storage st;
	Random num=new Random();
	
	Output(Storage st){
		this.st=st;
	}
	
	//System.out.println(num.nextInt(100));
	public void run() {
		while(true) {
			st.get(num.nextInt(100));
		}
	}
}
