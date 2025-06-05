package org.example;

public class Hanoi {

  public static void printTowers(Tower[] towers){
    for(Tower tower : towers){
      System.out.println("Tower 1: " + tower.toString());
    }
  }

  public static void main(String[] args) {
    Integer n_discs = 7;

    Tower[] towers = {new Tower(), new Tower(), new Tower()};

    Integer offset = 2;
    for(Integer ii=0; ii<n_discs; ii++){
      towers[0].push(new Disc(offset + n_discs - 1));
    }

    System.out.println("That was fun");
  }
}
