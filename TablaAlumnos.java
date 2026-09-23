import java.util.Random;
public class TablaAlumnos {
    public static void main(String[] args){
        Random random = new Random();
        int[][] matriz;
        int nF = 500;
        int nC = 6;
        matriz = new int[nF][nC];
        for (int i=0; i<nF; i++) {
            for (int j=0; j<nC; j++) {
                matriz[i][j] = random.nextInt(100 - 60 + 1) + 60;
            }
        }
        for (int i=0; i<(nF+1); i++) {
            for (int j=0; j<nC; j++) {
                if(j==0) {
                    if(i==0){
                        System.out.printf ("| %-10s |", "");
                    } else {
                        System.out.printf ("| %-10s |", "Alumno " + (i));
                    }
                }
                if(i==0){
                    System.out.printf ("| %-2s |", "Materia " + (j+1));
                } else {
                System.out.printf ("| %-9s |", matriz[i-1][j]);
                }
            }
        System.out.println("");
        }
        System.out.print ("Calificacion de Alumno 321 en su materia #5: " + (matriz[320][4]));
    }
}
