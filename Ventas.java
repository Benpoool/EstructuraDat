import java.util.Scanner;

public class Ventas {

    int[][] matriz;

    String[] meses = {
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };

    String[] departamentos = {
        "Ropa", "Deportes", "Jugueteria"
    };

    public Ventas() {
        matriz = new int[12][3];
    }

    public void insertar(int mes, int departamento, int venta) {
        matriz[mes][departamento] = venta;
    }

    public void buscar(int mes, int departamento) {
        System.out.println(
            "Venta de " + meses[mes] + " en " +
            departamentos[departamento] + ": $" +
            matriz[mes][departamento]
        );
    }

    public void eliminar(int mes, int departamento) {
        matriz[mes][departamento] = 0;

        System.out.println(
            "Venta eliminada correctamente."
        );
    }

    public void mostrar() {

        System.out.printf(
            "%-12s %-12s %-12s %-12s%n",
            "", "Ropa", "Deportes", "Jugueteria"
        );

        for (int i = 0; i < 12; i++) {

            System.out.printf("%-12s", meses[i]);

            for (int j = 0; j < 3; j++) {
                System.out.printf("%-12d", matriz[i][j]);
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        Ventas ventas = new Ventas();

        int opcion;

        ventas.mostrar();

        do {

            System.out.println("\nMENU");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opcion: ");
            opcion = scanner.nextInt();

            switch (opcion) {

                case 1:

                    System.out.println("\nSeleccione el mes:");

                    for (int i = 0; i < 12; i++) {
                        System.out.println((i + 1) + ". " + ventas.meses[i]);
                    }

                    System.out.print("Mes: ");
                    int mesInsertar = scanner.nextInt() - 1;

                    System.out.println("\nSeleccione el departamento:");

                    for (int i = 0; i < 3; i++) {
                        System.out.println((i + 1) + ". " + ventas.departamentos[i]);
                    }

                    System.out.print("Departamento: ");
                    int departamentoInsertar = scanner.nextInt() - 1;

                    System.out.print("Ingrese la venta: $");
                    int venta = scanner.nextInt();

                    ventas.insertar(
                        mesInsertar,
                        departamentoInsertar,
                        venta
                    );

                    System.out.println("Venta insertada correctamente.");

                    ventas.mostrar();

                    break;

                case 2:

                    System.out.println("\nSeleccione el mes:");

                    for (int i = 0; i < 12; i++) {
                        System.out.println((i + 1) + ". " + ventas.meses[i]);
                    }

                    System.out.print("Mes: ");
                    int mesBuscar = scanner.nextInt() - 1;

                    System.out.println("\nSeleccione el departamento:");

                    for (int i = 0; i < 3; i++) {
                        System.out.println((i + 1) + ". " + ventas.departamentos[i]);
                    }

                    System.out.print("Departamento: ");
                    int departamentoBuscar = scanner.nextInt() - 1;

                    ventas.buscar(
                        mesBuscar,
                        departamentoBuscar
                    );

                    break;

                case 3:

                    System.out.println("\nSeleccione el mes:");

                    for (int i = 0; i < 12; i++) {
                        System.out.println((i + 1) + ". " + ventas.meses[i]);
                    }

                    System.out.print("Mes: ");
                    int mesEliminar = scanner.nextInt() - 1;

                    System.out.println("\nSeleccione el departamento:");

                    for (int i = 0; i < 3; i++) {
                        System.out.println((i + 1) + ". " + ventas.departamentos[i]);
                    }

                    System.out.print("Departamento: ");
                    int departamentoEliminar = scanner.nextInt() - 1;

                    ventas.eliminar(
                        mesEliminar,
                        departamentoEliminar
                    );

                    ventas.mostrar();

                    break;

                case 4:

                    System.out.println("Programa finalizado.");

                    break;

                default:

                    System.out.println("Opcion no valida.");

            }

        } while (opcion != 4);

        scanner.close();
    }
}
