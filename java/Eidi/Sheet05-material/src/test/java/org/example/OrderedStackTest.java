package org.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

public class OrderedStackTest {
  @Test
  void test_push(){
    OrderedStack<Disc> SUT = new OrderedStack<>();
    Disc disc1 = new Disc(3);
    Disc disc2 = new Disc(2);

    SUT.push(disc1).push(disc2);

    assertEquals(disc2, SUT.peek());
    assertEquals(disc2, SUT.pop());
    assertEquals(disc1, SUT.peek());
    assertEquals(disc1, SUT.pop());
  }
    @Test
    void test_push_throws() {
      OrderedStack<Disc> SUT = new OrderedStack<>();
      Disc disc1 = new Disc(3);
      Disc disc2 = new Disc(5);      
      
      assertThrows(IllegalStateException.class, () -> SUT.push(disc1).push(disc2));
    }
}
