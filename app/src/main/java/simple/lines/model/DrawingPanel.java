package simple.lines.model;


import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.List;
import java.util.Map;
import java.util.Random;
import simple.lines.model.Point;

import javax.swing.JPanel;

public class DrawingPanel extends JPanel {
    List<List<Point>> reworkedLineSegments;

    public DrawingPanel(List<List<Point>> reworkedLineSegments) {
        this.reworkedLineSegments = reworkedLineSegments;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        Random rand = new Random();

        g2d.translate(0, getHeight());
        g2d.scale(1, -1);

        for (List<Point> segment : reworkedLineSegments) {
            // Set a random color for each segment
            g2d.setColor(new Color(rand.nextInt(256), rand.nextInt(256), rand.nextInt(256)));

            for (int i = 0; i < segment.size() - 1; i++) {
                Point p1 = segment.get(i);
                Point p2 = segment.get(i + 1);
                g2d.drawLine(Math.round(p1.getX()), Math.round(p1.getY()), Math.round(p2.getX()), Math.round(p2.getY()));
            }
        }
    }
}