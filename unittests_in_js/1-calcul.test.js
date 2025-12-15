const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {

  // --- SUM Tests ---
  describe('when type is SUM', () => {
    // Basic test case with rounding both up
    it('should return 6 when a is 1.4 and b is 4.5', () => {
      // 1.4 rounds to 1, 4.5 rounds to 5. Result: 1 + 5 = 6
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    // Test case with rounding both down
    it('should return 5 when a is 1.2 and b is 3.4', () => {
      // 1.2 rounds to 1, 3.4 rounds to 3. Result: 1 + 3 = 4
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.4), 4);
    });

    // Test case with one integer and one rounded down
    it('should return 5 when a is 2 and b is 2.2', () => {
      // 2 rounds to 2, 2.2 rounds to 2. Result: 2 + 2 = 4
      assert.strictEqual(calculateNumber('SUM', 2, 2.2), 4);
    });

    // Test case with negative numbers and rounding
    it('should return 0 when a is -1.5 and b is 1.5', () => {
      // -1.5 rounds to -1, 1.5 rounds to 2. Result: -1 + 2 = 1
      assert.strictEqual(calculateNumber('SUM', -1.5, 1.5), 1);
    });
  });

  // --- SUBTRACT Tests ---
  describe('when type is SUBTRACT', () => {
    // Basic test case with rounding both up
    it('should return -4 when a is 1.4 and b is 4.5', () => {
      // 1.4 rounds to 1, 4.5 rounds to 5. Result: 1 - 5 = -4
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    // Test case resulting in a positive number
    it('should return 2 when a is 5.8 and b is 3.2', () => {
      // 5.8 rounds to 6, 3.2 rounds to 3. Result: 6 - 3 = 3
      assert.strictEqual(calculateNumber('SUBTRACT', 5.8, 3.2), 3);
    });

    // Test case involving zero
    it('should return 3 when a is 3.4 and b is 0.4', () => {
      // 3.4 rounds to 3, 0.4 rounds to 0. Result: 3 - 0 = 3
      assert.strictEqual(calculateNumber('SUBTRACT', 3.4, 0.4), 3);
    });
  });

  // --- DIVIDE Tests ---
  describe('when type is DIVIDE', () => {
    // Basic test case
    it('should return 0.2 when a is 1.4 and b is 4.5', () => {
      // 1.4 rounds to 1, 4.5 rounds to 5. Result: 1 / 5 = 0.2
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    // Test case resulting in an integer
    it('should return 2 when a is 6.2 and b is 2.9', () => {
      // 6.2 rounds to 6, 2.9 rounds to 3. Result: 6 / 3 = 2
      assert.strictEqual(calculateNumber('DIVIDE', 6.2, 2.9), 2);
    });

    // Test case for division by 1
    it('should return 7 when a is 7.4 and b is 0.7', () => {
      // 7.4 rounds to 7, 0.7 rounds to 1. Result: 7 / 1 = 7
      assert.strictEqual(calculateNumber('DIVIDE', 7.4, 0.7), 7);
    });

    // Edge Case: Division by zero
    it('should return "Error" when rounded b is 0 (b=0)', () => {
      // 1.4 rounds to 1, 0 rounds to 0. Result: Error
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    // Edge Case: Division by zero when b is rounded down to 0
    it('should return "Error" when rounded b is 0 (b=0.4)', () => {
      // 1.4 rounds to 1, 0.4 rounds to 0. Result: Error
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });

    // Edge Case: Division by zero when b is rounded up to 0 (negative)
    it('should return "Error" when rounded b is 0 (b=-0.4)', () => {
      // 1.4 rounds to 1, -0.4 rounds to 0. Result: Error
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.4), 'Error');
    });
  });
});
