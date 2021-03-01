function distributeCandies(candyType: number[]): number {
    const canEatCandies = candyType.length / 2;
    
    const set = new Set();
    for (const candy of candyType) {
        set.add(candy)
    }
    
    
    if (set.size > canEatCandies) {
        return canEatCandies
    }
    
    return set.size
}