import jwt

encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MDM0OTYzNTcsIm5hbWUiOiJCYXNrYXJhbiBQYW5uZWVyc2VsdmFtIiwibW9iaWxlX25vIjoiKzkxOTg0MzU1MjA2NSIsInN0YXR1c19jb2RlIjozMDAsImNvbG9yX2NvZGUiOiIjM0FBODRDIiwibWVzc2FnZSI6IkJhc2thcmFuIFBhbm5lZXJzZWx2YW0gKCs5MTk4NDM1NTIwNjUpIGlzIHNhZmUifQ.OrmPb-ASsPe_LMMCfxL06NXerm9RXDm2V_vaG80hgMlwuK46gtJwAv0A8SV2ZM-OBP-0IDnY9Upbi3xIak46YiFbQ00m2Da71hzGJpc119WyrwuQUc5Q-LV-TG0iKsD6OvZR7p1SxscgEuijBuuya_RpLnKbRbD8CyND2-e7hlxuEcNT2pADffsomC9p_NIP0iRTh40MBK3wYnbJ3EL3QmOcHGSp6mYOd5jVUbRNtTrSrU4uuuLzMmSWwabOb9PFhgO7dH2HWjLOf5t_80ptlKvDKHzIDFUMddkYUahMeO2g6JrudVOLotXoUKRWfXSMxeBSBiDHoGP8NghDsy8nr8nc9f3TT0UFtVhXHquFHyc13DjGXmFXQG58v0rls1HQE2VwIalmJiaCShVshaK31wid61nszcmM1Z2Hu7Ry_-h1DVjGBxZTMj-nfYTp8sxaiSSPxEJmDUn8eP2Hf9Rigb0BXZi8Fd5RhQ6D23hCUv5qFnbBbe85eD43vPQ0wcJpEhtRK0tJgYXeNFymV7DcC254YS8JWKY55FjDIhw3VtVIHG0R4BhsuRy2d_-i0ft0U4xw4BFDfBZg6or-z0OfsVc_04napqEV80NPRPe0ys2pRQY-8ZMG8GnIyl0_tHhTP-mCUXjVCYXxcUPvDJ6fQQOuZfB6rJvCMkbEkVNlJWQ"


key='''your key here'''


def decrypt(token):
    dec = jwt.decode(token, key, verify = True, algorithms=['RS256'])
    return dec
