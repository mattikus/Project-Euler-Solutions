fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
answer = sum . takeWhile (<4000000) $ filter even fibs 
main = putStrLn $ "Problem 2 Answer: " ++ show answer
