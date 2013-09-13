#ifndef ___EDITDISTANCE__H__
#define ___EDITDISTANCE__H__

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

struct PatternMap {
    uint64_t p_[256][4];
    unsigned int tmax_;
    unsigned int tlen_;
};


unsigned int edit_distance(int64_t const *a, unsigned int const asize, int64_t const *b, unsigned int const bsize);
void create_patternmap(PatternMap *pm, int64_t const *a, unsigned int const size);
unsigned int edit_distance_by_patternmap(PatternMap *mp, const int64_t *b, const unsigned int size);

#ifdef __cplusplus
}
#endif

#endif
