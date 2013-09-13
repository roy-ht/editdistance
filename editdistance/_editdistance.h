#ifndef ___EDITDISTANCE__H__
#define ___EDITDISTANCE__H__

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// struct PatternMap {
//     uint64_t p_[256][4];
//     unsigned int tmax_;
//     unsigned int tlen_;
// };

unsigned int edit_distance(const int64_t *a, const unsigned int asize, const int64_t *b, const unsigned int bsize);
// void create_patternmap(struct PatternMap *pm, const int64_t *a, const unsigned int size);
// unsigned int edit_distance_by_patternmap(struct PatternMap *mp, const int64_t *b, const unsigned int size);

#ifdef __cplusplus
}
#endif

#endif
