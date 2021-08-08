#include<vector>
#include "Block.h"
#include<cstdint>

class Blockchain {
private:
	uint32_t _nDifficulty;
	std::vector<Block> _vChain;
	Block _GetLastBlock() const;

public:
	Blockchain();
	void AddBlock(Block bNew);
};
