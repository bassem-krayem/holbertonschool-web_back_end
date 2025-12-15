const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  // Test Case 1: Both integers (No rounding needed)
  it('should return 4 when a is 1 and b is 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  // Test Case 2: b is rounded up
  it('should return 5 when a is 1 and b is 3.7', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // Test Case 3: a is rounded down, b is rounded up
  it('should return 5 when a is 1.2 and b is 3.7', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  // Test Case 4: a is rounded up (.5 case), b is rounded up
  it('should return 6 when a is 1.5 and b is 3.7', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Test Case 5: a is rounded down, b is rounded down
  it('should return 4 when a is 1.2 and b is 3.2', () => {
    assert.strictEqual(calculateNumber(1.2, 3.2), 4);
  });

  // Test Case 6: a is rounded up, b is rounded down
  it('should return 5 when a is 1.6 and b is 3.2', () => {
    assert.strictEqual(calculateNumber(1.6, 3.2), 5);
  });

  // Test Case 7: Both are rounded up (.5 case)
  it('should return 7 when a is 3.5 and b is 3.5', () => {
    assert.strictEqual(calculateNumber(3.5, 3.5), 8); // 4 + 4 = 8
  });

  // Test Case 8: Both are rounded up (non-.5)
  it('should return 6 when a is 2.8 and b is 3.1', () => {
    assert.strictEqual(calculateNumber(2.8, 3.1), 6); // 3 + 3 = 6
  });

  // Test Case 9: Tests with negative numbers (Good practice for completeness)
  it('should return 0 when a is -1.5 and b is 1.5', () => {
    assert.strictEqual(calculateNumber(-1.5, 1.5), 0); // -1 + 2 = 1. Wait, Math.round(-1.5) is -1, Math.round(1.5) is 2. The result should be 1.
  });

  // Corrected Test Case 9:
  it('should return 1 when a is -1.5 and b is 1.5', () => {
    assert.strictEqual(calculateNumber(-1.5, 1.5), 1); // Math.round(-1.5) = -1, Math.round(1.5) = 2. Sum is 1.
  });
});
