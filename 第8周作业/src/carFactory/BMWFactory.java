package carFactory;
import car.*;

public class BMWFactory implements CarFactory{

	public Car produceCar() {
		return new BMW();
	}
}
