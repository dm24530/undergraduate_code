package carfactory;

import car.Audi;
import car.Benz;
import car.Car;

public class BenzFactory implements CarFactory {

	@Override
	public Car produceCar() {
		// TODO Auto-generated method stub
		return new Benz();
	}

}
