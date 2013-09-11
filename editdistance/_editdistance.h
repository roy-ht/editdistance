#ifndef ___EDITDISTANCE__H__
#define ___EDITDISTANCE__H__

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

enum MAPOPTION {
    MAPOPTION_MAP,
    MAPOPTION_N1,
    MAPOPTION_N2
};

unsigned int edit_distance(int64_t const *a, unsigned int const asize, int64_t const *b, unsigned int const bsize, enum MAPOPTION const opt);

#ifdef __cplusplus
}
#endif

#endif
