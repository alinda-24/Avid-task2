package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

class Player {
    private String name;
    private int position;
    private int score;

    public Player(String name, int position, int score) {
        this.name = name;
        this.position = position;
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public void move(int distance) {
        this.position += distance;
        System.out.println(name + " moved to position " + this.position);
    }

    public void updateScore(int points) {
        this.score += points;
        System.out.println(name + "'s new score is " + this.score);
    }

    public void printInfo() {
        System.out.println("Player: " + name + ", Position: " + position + ", Score: " + score);
    }
}