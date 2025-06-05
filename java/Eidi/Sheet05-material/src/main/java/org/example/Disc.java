package org.example;

public class Disc implements Comparable<Disc> {

    private final Integer size;

    public Disc(Integer size){ this.size = size; }

    @Override
    public int compareTo(Disc disc) {
        return size.compareTo(disc.size);
    }
}
