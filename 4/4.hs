import List

isPalin :: Integer -> Bool
isPalin x = (reverse $ show x) == show x
palins = sort [x * y | x <- [100..999], y <- [100..999], isPalin (x*y)]
answer = last palins
main = putStrLn $ "Problem 4 Answer: " ++ show answer
