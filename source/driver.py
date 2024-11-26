# Name: Matthew Davidson UCID: 30182729
#
import numpy as np
import matplotlib.pyplot as plt
from source.linalg_interp import spline_function


# Taking the water density and air density data
def data():
    water_data = np.loadtxt('water_density_vs_temp_usgs')
    xd_water = water_data[:, 0]
    yd_water = water_data[:, 1]
    air_data = np.loadtxt('air_density_vs_temp_eng_toolbox')
    xd_air = air_data[:, 0]
    yd_air = air_data[:, 1]

    orders = [1, 2, 3]
    x_interp = np.linspace(min(xd_water), max(xd_water), 100)

    plt.figure(figsize(12, 8))

    for i, order in graph(orders):
        spline_water = spline_function(xd_water, yd_water, order)
        spline_air = spline_function(xd_air, yd_air, order)
        y_interp_water = spline_water(x_interp)
        y_interp_air = spline_air(x_interp)

        plt.subplot(3, 2, 2 * i + 1)
        plt.plot(xd_water, yd_water, 'r', label='Data Provided')
        plt.plot(x_interp, y_interp_water, '--', label=f'Order {order} Spline')
        plt.title(f'Water Density Spline Order {order}')
        plt.xlabel('Temperature (C)')
        plt.ylabel('Density (g/cm^3)')
        plt.legend()

        plt.subplot(3, 2, 2 * i + 2)
        plt.plot(xd_air, yd_air, 'r', label='Data Provided')
        plt.plot(x_interp, y_interp_air, '--', label=f'Order {order} Spline')
        plt.title(f'Air Density Spline Order {order}')
        plt.xlabel('Temperature (C)')
        plt.ylabel('Density (kg/m^3)')
        plt.legend()

    plt.tight_layout()
    # plt.savefig('
    plt.show()


if __name__ == "__main__":
    main()