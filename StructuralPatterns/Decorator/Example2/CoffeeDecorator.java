// Abstract class for decorating Coffee objects, allowing additional features to be added while preserving core functionality.

package Decorator;

public abstract class CoffeeDecorator implements Coffee {
    protected Coffee coffee;

    public CoffeeDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    @Override
    public String getDescription() {
        // TODO: Complete this method to return the description of the decorated coffee.
        return this.coffee.getDescription();
        
    }

    @Override
    public double getCost() {
        // TODO: Complete this method to return the cost of the decorated coffee.
        return this.coffee.getCost();
        
    }
}