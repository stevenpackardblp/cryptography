# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import annotations

INCLUDES = """
#include <openssl/bn.h>
"""

TYPES = """
static const long Cryptography_HAS_BN_FLAGS;

typedef ... BN_CTX;
typedef ... BN_MONT_CTX;
typedef ... BIGNUM;
typedef int... BN_ULONG;
"""

FUNCTIONS = """
#define BN_FLG_CONSTTIME ...

void BN_set_flags(BIGNUM *, int);

BIGNUM *BN_new(void);
void BN_free(BIGNUM *);
void BN_clear_free(BIGNUM *);

int BN_rand_range(BIGNUM *, const BIGNUM *);

BN_CTX *BN_CTX_new(void);
void BN_CTX_free(BN_CTX *);

void BN_CTX_start(BN_CTX *);
BIGNUM *BN_CTX_get(BN_CTX *);
void BN_CTX_end(BN_CTX *);

BN_MONT_CTX *BN_MONT_CTX_new(void);
int BN_MONT_CTX_set(BN_MONT_CTX *, const BIGNUM *, BN_CTX *);
void BN_MONT_CTX_free(BN_MONT_CTX *);

int BN_set_word(BIGNUM *, BN_ULONG);

char *BN_bn2hex(const BIGNUM *);
int BN_hex2bn(BIGNUM **, const char *);

int BN_bn2bin(const BIGNUM *, unsigned char *);
BIGNUM *BN_bin2bn(const unsigned char *, int, BIGNUM *);

int BN_num_bits(const BIGNUM *);

int BN_is_negative(const BIGNUM *);
int BN_is_odd(const BIGNUM *);
int BN_mod_exp_mont(BIGNUM *, const BIGNUM *, const BIGNUM *, const BIGNUM *,
                    BN_CTX *, BN_MONT_CTX *);
int BN_mod_exp_mont_consttime(BIGNUM *, const BIGNUM *, const BIGNUM *,
                              const BIGNUM *, BN_CTX *, BN_MONT_CTX *);
BIGNUM *BN_mod_inverse(BIGNUM *, const BIGNUM *, const BIGNUM *, BN_CTX *);

int BN_num_bytes(const BIGNUM *);

/* The following 3 prime methods are exposed for Tribler. */
int BN_generate_prime_ex(BIGNUM *, int, int, const BIGNUM *,
                         const BIGNUM *, BN_GENCB *);
int BN_is_prime_ex(const BIGNUM *, int, BN_CTX *, BN_GENCB *);
const int BN_prime_checks_for_size(int);
"""

CUSTOMIZATIONS = """
#if CRYPTOGRAPHY_IS_BORINGSSL
static const long Cryptography_HAS_BN_FLAGS = 0;

static const int BN_FLG_CONSTTIME = 0;
void (*BN_set_flags)(BIGNUM *, int) = NULL;
int (*BN_prime_checks_for_size)(int) = NULL;
#else
static const long Cryptography_HAS_BN_FLAGS = 1;
#endif
"""
