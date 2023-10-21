# opencv
//This is a homework
package com.itheima.opencv;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.highgui.HighGui;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

import java.util.Arrays;

public class opencore {
    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    public static void main(String[] args) {
         System.out.println(Core.VERSION);//确认环境是否配置成功
         double[] a=new double[512];
         int count=0;
        Mat src1= Imgcodecs.imread("C:\\Users\\22170\\Desktop\\Lena.jpg");
        Imgproc.cvtColor(src1,src1,Imgproc.COLOR_RGB2GRAY);//灰度图
        // 输出矩阵的行数和列数
        int rows = src1.rows();
        int cols = src1.cols();
        System.out.println("Rows: " + rows);
        System.out.println("Cols: " + cols);

        // 输出矩阵的像素值
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                double[] pixel = src1.get(row, col);
                double value = pixel[0];
                System.out.print(value + " ");
            }
            System.out.println();
        }
        //计算前两行平均值
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < 2; j++) {
                double[] pixel  = src1.get(i, j);
                 a[count]=pixel[0];
                 count++;
            }
        }
        // 计算平均值
        double average = calculateAverage(a);
        System.out.println("Average: " + average);

        // 计算中位数
        double median = calculateMedian(a);
        System.out.println("Median: " + median);


        Mat mat3 = new Mat(256,256,CvType.CV_8UC3);
        Mat top = mat3.submat(0,128,0,256);
        Mat bottom = mat3.submat(128,256,0,256);
        Mat totop = Imgcodecs.imread("C:\\Users\\22170\\Desktop\\lena.one11.jpg");
        Mat tobottom = Imgcodecs.imread("C:\\Users\\22170\\Desktop\\lena.gray1.jpg");

        totop.copyTo(top);
        tobottom.copyTo(bottom);








        Mat mat1=new Mat();
        Mat mat2=new Mat();


        Imgproc.threshold(src1,mat1,average,255,Imgproc.THRESH_BINARY);
        Imgproc.threshold(src1,mat2,median,255,Imgproc.THRESH_BINARY);//二值图
        //Imgcodecs.imwrite("lena.gray.jpg",src1);
        //Imgcodecs.imwrite("lena.one1.jpg",mat1);
        //Imgcodecs.imwrite("lena.two2.jpg",mat2);
        //Imgcodecs.imwrite("jiafen.jpg",mat3);
        HighGui.imshow("lena.gray",src1);
        HighGui.waitKey(0);
        HighGui.imshow("lena.one",mat1);
        HighGui.waitKey(0);
        HighGui.imshow("lena.two",mat2);
        HighGui.waitKey(0);



    }
    public static double calculateAverage(double[] array) {
        double sum = 0.0;
        for (double num : array) {
            sum += num;
        }
        return sum / array.length;
    }

    public static double calculateMedian(double[] array) {
        Arrays.sort(array);
        int n = array.length;
        if (n % 2 == 0) {
            double mid1 = array[n / 2 - 1];
            double mid2 = array[n / 2];
            return (mid1 + mid2) / 2.0;
        } else {
            return array[n / 2];
        }
    }
}
