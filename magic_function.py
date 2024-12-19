import logging

logging.basicConfig(level=logging.INFO)

class Calculator:
   
    
    def add(self, a, b):
      
        return a + b
    
    def subtract(self, a, b):
       
        return a - b
    
    def multiply(self, a, b):
      
        return a * b
    
    def divide(self, a, b):
        
        try:
            return a / b
        except ZeroDivisionError as e:
            logging.error("Division by zero error")
            return None

def main():
    calc = Calculator()
    
    logging.info("3 + 5 = %d", calc.add(3, 5))
    logging.info("10 - 2 = %d", calc.subtract(10, 2))
    logging.info("4 * 7 = %d", calc.multiply(4, 7))
    logging.info("8 / 0 = %s", calc.divide(8, 0))

if __name__ == "__main__":
    main()
