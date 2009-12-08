primes = 2 : filter isPrime [3,5..]
isPrime n = not . any (`isDiv` n) . takeWhile (\x -> x^2 <= n) $ primes
isDiv a b = b `mod` a == 0

answer = sum $ takeWhile (<2000000) primes
main = putStrLn $ show answer
