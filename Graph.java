import java.awt.*;  
import javax.swing.JFrame;  

public class Graph extends Canvas {

    private JFrame frame;
    private Axis axis;

    private double[] data = {0,1,4,9,2,2,2,3,6,78,5,3,5,2,4,3,2,35,5,7,9,5,3,6,7,8,5,0};

    public Graph() {
        super();
        createWindow();
        this.axis = new Axis();
    }

    public void drawGraph(Graphics g) {
        int xStep = (axis.endX - axis.originX)/data.length;
        int yStep = getYStep();
        for(int x = 0; x<data.length-1; x++) {
            g.drawLine(
                (x*xStep)+axis.originX,
                axis.originY-(int)data[x]*yStep,
                ((x+1)*xStep)+axis.originX,
                axis.originY-(int)data[x+1]*yStep);
        }
    }

    public int getYStep() {
        double largest = 0;
        for (double value : data) {
            if(value>largest) {
                largest = value;
            }
        }
        int i = (-(axis.endY - axis.originY))/(int)largest;
        return i;
    }

    public void createWindow() {
        frame = new JFrame();
        frame.setTitle("Graph");
        frame.setMinimumSize(new Dimension(400,400));
        frame.add(this);
        frame.setVisible(true);  
    }

    @Override
    public void update(Graphics g) {
        axis.drawAxis(g);
        drawGraph(g);
    }

    public static void main(String[] args) throws Exception {
        Graph graph = new Graph();
        while(true) {
            graph.repaint();
        }
    }
  


    private class Axis {
        private int originX, originY;
        private int endX, endY;

        public Axis() {
            this.originX = 50;
            this.originY = frame.getHeight() - 100;
            this.endX = frame.getWidth() - 50;
            this.endY = 50;
        }

        public void adjustAxis() {
            this.originY = frame.getHeight() - 100;
            this.endX = frame.getWidth() - 50;
        }

        public void drawAxis(Graphics g) {
            adjustAxis();
            g.drawLine(originX, originY, originX, endY);
            g.drawLine(originX, originY, endX, originY);
        }
    }
}
