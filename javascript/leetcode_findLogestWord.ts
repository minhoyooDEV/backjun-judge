function findLongestWord(s: string, d: string[]): string {
    if (!d.length) {
        return ''
    }
    const orderedD = d.sort()
    const countBoard = Array(d.length).fill(0);
    
    s.split('').forEach(v => {
        orderedD.forEach((data, index) => {
            if (v === data[countBoard[index]]){
                countBoard[index] += 1
            }
        }) 
    })
    const maxCount = Math.max(...countBoard)
    if (maxCount === 0) {
        return ''
    }
    console.log(orderedD)
    
    const targetIndex = countBoard.findIndex(count => count === maxCount);

    console.log(targetIndex)
    
    return orderedD[targetIndex]
    
};