package carfactory;

import car.Audi;
import car.Car;

public class AudiFactory implements CarFactory{

	@Override
	public Car produceCar() {
		// TODO Auto-generated method stub
		return new Audi();
	}

}
