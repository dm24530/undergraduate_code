package carfactory;

import car.Audi;
import car.BMW;
import car.Car;

public class BMWFactory implements CarFactory{

	@Override
	public Car produceCar() {
		// TODO Auto-generated method stub
		return new BMW();
	}

}
