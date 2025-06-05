package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StackTest {

    @Test
    void test_push() {
        Stack<Integer> stack = new Stack<>();
        stack.push(1).push(2).push(3).push(4).push(5).push(6);
        assertEquals(6, stack.peek().intValue());
        assertEquals(6, stack.pop().intValue());
        assertEquals(5, stack.pop().intValue());
        assertEquals(4, stack.pop().intValue());
    }
}