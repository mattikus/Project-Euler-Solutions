import Char

answer = sum [digitToInt x | x <- show $ product [1..100]]
main = putStrLn $  "Problem 20 Answer: " ++ show answer
