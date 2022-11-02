from utils.logger import logger

class BaseAssert:
    @classmethod#使用类名就可以直接调用类方法
    def define_assert(cls, res, respData):
        try:
            if 'code' in respData:
                assert res['code'] == respData['code']
            elif 'msg' in respData:
                assert res['msg'] == respData['msg']
            else:
                assert res.get('error') == respData['error']
        except Exception as error:
            logger.info(res)
            raise error