#include "Block.h"
#include "SHA256.h"
#include<sstream>

Block::Block(uint32_t nIndexIn, const std::string& sDataIn) : _nIndex(nIndexIn), _sData(sDataIn) {
	_nNonce = -1;
	_tTime = time(nullptr);
}

std::string Block::GetHash() {
	return _sHash;
}

void Block::MineBlock(uint32_t nDifficulty) {
	char cstr[257];
	memset(cstr, '0', 257);
	cstr[nDifficulty] = '\0';

	string str(cstr);
	do {
		_nNonce++;
		_sHash = _CalculateHash();
	} while (_sHash.substr(0, nDifficulty) != str);

	cout << "Block mined!: " << _sHash << endl;
}

inline string Block::_CalculateHash() const {
	stringstream ss;
	ss << _nIndex << _tTime << _sData << _nNonce << sPrevHash;

	return sha256(ss.str());
}