package org.example;

public class Hanoi {
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
