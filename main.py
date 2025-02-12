Creating an eco-delivery optimizer involves developing a system that can intelligently route delivery vehicles in a way that minimizes fuel consumption and emissions. This might require integrating with various data sources such as traffic data, road conditions, and vehicle specifications. Below is a simplified version of such a program using Python. For a full-scale implementation, you might need more advanced tools and third-party services.

```python
import random

class EcoDeliveryOptimizer:
    def __init__(self):
        # Here you typically initialize connections to APIs, load data sets, etc.
        self.routes = []  # This will store possible routes
        self.best_route = None
    
    def load_data(self):
        """
        Simulates loading data from various sources needed for geospatial analysis
        """
        print("Loading data...")
        # Here you would typically load data from files, databases, or APIs
        # This could include traffic, road conditions, and vehicle data
        # Simulating with sleep and a print statement
        pass

    def calculate_emissions(self, route):
        """
        Calculate emissions for a given route.
        For simplicity, we assume emissions value is random for this mock.
        """
        # Normally, you would calculate based on traffic, distance, speed, stops, etc.
        return random.uniform(1, 100)  # Emissions in arbitrary units

    def calculate_fuel_consumption(self, route):
        """
        Calculate fuel consumption for a given route.
        For simplicity, we assume fuel consumption is also random for this mock.
        """
        # Normally, you would calculate based on fuel efficiency, distance, etc.
        return random.uniform(1, 50)  # Fuel consumption in arbitrary units

    def find_routes(self, source, destination):
        """
        Generates possible routes from source to destination.
        In a real system, you might use a graph-based search algorithm or an API.
        """
        print(f"Finding routes from {source} to {destination}...")
        # Here we would generate and return possible routes.
        # This is a mock with randomly generated routes.
        self.routes = [f"Route {i}" for i in range(5)]

    def optimize_route(self):
        """
        Optimize to find the route with the lowest emissions and fuel consumption.
        """
        try:
            if not self.routes:
                raise ValueError("No routes found to optimize")

            lowest_emission = float('inf')
            best_route = None

            for route in self.routes:
                emissions = self.calculate_emissions(route)
                fuel = self.calculate_fuel_consumption(route)
                print(f"Evaluating {route}: Emissions={emissions}, Fuel={fuel}")

                if emissions < lowest_emission:
                    lowest_emission = emissions
                    self.best_route = route

            if self.best_route is None:
                raise RuntimeError("Failed to find an optimal route")

            print(f"Best route: {self.best_route} with emissions score of {lowest_emission}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except RuntimeError as re:
            print(f"Error: {re}")
        except Exception as e:
            # Catch any other unforeseen exceptions
            print(f"An unexpected error occurred: {e}")

def main():
    optimizer = EcoDeliveryOptimizer()
    optimizer.load_data()
    source = "Warehouse A"
    destination = "Customer B"
    optimizer.find_routes(source, destination)
    optimizer.optimize_route()

if __name__ == "__main__":
    main()
```

### Notes:
- **Routing Logic**: This simplified version uses fake `(random)` data. Implementing real routing would likely require geospatial libraries or services (e.g., Google Maps or OpenStreetMap).
- **Error Handling**: Basic error handling is provided for cases where no routes are found or optimization fails.
- **Further Improvements**: This mock setup would be enhanced in a professional application to include:
  - Real geospatial data and API integration.
  - A real transportation network model and route selection implementation.
  - Advanced fuel and emissions calculations aligning with the types of vehicles and routes.