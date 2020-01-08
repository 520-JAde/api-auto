from common.configHttp import RunMain


class Interface:

    def login(self, method, url, data, header=None):
        """登录接口"""
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def newcustomer(self, header=None):
        """新增客户"""
        url = 'http://test.api.neurongenius.com/api/v1/customer/add?reportId='
        data = '{"preUserName":"","preUserId":"","preDate":null,"preRemark":"","preId":"","photoUrl":"","sex":2,"name":"u9","nickName":[],"phoneNumber":[{"phoneNumber":"17311330109","ismain":true}],"storeId":"","sourceType":5,"sourceTypeOldNew":"","sourceTypeUserId":"","sourceTypeOther":"","sourceTypeRemark":"","sysUserId":"9d84c6ac6e0d2696ba815c935408417e","customerPoolType":1,"poolId":"0e61d5093b6ce4488e3835854af66fb7","birthday":"","age":"","marriedFlag":null,"fertilityFlag":null,"area":[],"sourceTypeDetailType":"","allergyLabels":[],"personalityLabels":[],"associatedDoctors":[],"relatedDoctors":[],"relatedServices":[],"relatedConsultants":[]}'
        # data = eval(data)
        print(type(data))
        method = 'post'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def order(self, header=None):
        """新增预约"""
        url = 'http://test.api.neurongenius.com/api/v2/bespeak/add'
        data = '{"anaesthesia":"[]","fileId":"[]","startTime":"2020-01-03 17:00:00","endTime":"2020-01-03 17:30:00","expertId":"c0cb8e33ab2f1e0e3cf7b7a2a55eb01f","expertName":"YT","customerId":"7528c1297a9f57cd5786487197a552cf","bespeakTypeValue":"1","bespeakTypeName":"咨询","bespeakTypeColor":"#98d8a6","operationFlag":false,"inviteId":"9d84c6ac6e0d2696ba815c935408417e","inviteName":"YT","bespeakUserId":"9d84c6ac6e0d2696ba815c935408417e","bespeakUserName":"YT","bespeakProject":[{"dataType":1,"dataId":"04a4a7b39efb6221db26b9ea3bfebd2a","dataName":"皮肤科"}]}'
        data = data.encode()
        method = 'post'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def sure(self, header=None):
        """预约确认"""
        url = "http://test.api.neurongenius.com/api/v2/bespeak/confirmed?id="
        data = '8cd84957e45a499c886815f38155d914'
        method = 'put'

    def reception(self, header=None):
        """新增接待"""
        url = "http://test.api.neurongenius.com/api/v2/reception/add"
        data1 = '{"immediateTreatFlag":false,"receptionType":"1","receptionProject":"[{\"dataType\":1,\"dataId\":\"04a4a7b39efb6221db26b9ea3bfebd2a\",\"dataName\":\"皮肤科\"}]","triageToUserId":"9d84c6ac6e0d2696ba815c935408417e","receiverId":"9d84c6ac6e0d2696ba815c935408417e","assistReceiverId":"","urgentFlag":false,"remark":"","bespeakId":"62f74a7f70934fdcaefe025de8b1279d","customerId":"7528c1297a9f57cd5786487197a552cf","receptionTypeName":"咨询","assistReceiverName":"","receiverName":"YT","triageToUserName":"YT"}'
        data = data1.encode()
        method = 'post'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def consultation(self, header=None):
        """新增咨询"""
        url = 'http://test.api.neurongenius.com/api/v1/flowbrandinfo/turnTo'
        data = '{"customerId":"7528c1297a9f57cd5786487197a552cf","userId":"9d84c6ac6e0d2696ba815c935408417e","id":"13769a1c30dc75b9fd63d07d4575e1bf","opType":1,"proIds":[],"proTypes":[]}'
        method = 'post'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def cashier(self, header=None):
        """
        开订单
        :param header:
        :return:
        """
        url = "http://test.api.neurongenius.com/api/v1/billing/addV2"
        data = '{"billing":{"approvalFlag":false,"forceApproveFlag":false,"customerId":"7528c1297a9f57cd5786487197a552cf","billingUserId":"9d84c6ac6e0d2696ba815c935408417e"},"billingProjects":[{"id":"826295b02dde11ea97ce9d205cf88c0d","projectId":"44d985261d0862a22be2232644127e89","projectName":"看看","freeFlag":false,"discount":10,"numberOfTime":1,"departmentId":"","departmentName":"","doctorId":"","orderOriginalPrice":1800,"totalPrice":1800}],"payment":{"approvalFlag":false,"shouldPayMoney":1800,"billingExplain":"","payBillingUserId":"9d84c6ac6e0d2696ba815c935408417e"},"paymentItemList":[{"selectFlag":true,"dataId":"967f6352618cce9d2a7cbac95dd21d36","paymentItemMark":0,"departmentId":null,"departmentName":null,"doctorId":null,"doctorName":null,"uncollectedPrice":0,"totalPrice":1800,"thisChargePrice":1800,"todayTreatFlag":false}]}'
        data = data.encode()
        method = 'put'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def payment(self, header=None):
        """
        缴费
        :param header:
        :return:
        """
        url = "http://test.api.neurongenius.com/api/v1/payment/payFee"
        data = '{"invoiceFlag":false,"payWay":[{"payMode":"WECHAT","payMoney":1800}],"depositReqList":[],"balanceReqList":[],"paymentId":"213e9579c0d94ba3b7494f2845e04b3b","chargeUserId":"9d84c6ac6e0d2696ba815c935408417e","chargeUserName":"YT"}'
        method = 'put'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response

    def verification(self, header=None):
        """
        核销
        :param header:
        :return:
        """
        url = 'http://test.api.neurongenius.com/api/v1/treatment/singleDeductAndVerification'
        data = '{"id":"77bc21b99ea2a67d26e4955b7bc6ce69","treatDept":{"label":"无创科","key":"69264e8f851865d91d20f98736176cea"},"treatmentTime":"2020-01-02T06:18:31.494Z","verificationDept":{"label":"皮肤科","value":"bfb24660a14d9be2f9d2e7a0af7e4b87"},"verificationUser":{"label":"YT","key":"9d84c6ac6e0d2696ba815c935408417e"},"verifications":[{"materialId":"04da937370735b268100e36da2fe678a","verificationNumber":0,"materialUnit":"1","extraFlag":true,"specification":"11*66","warehouseId":"c032adccd924717f6d623c616f0e83c7"}],"treatmentDeviceList":[],"verificationFlag":true,"deductFlag":false,"treatmentDoctorList":[{"roleName":"医生","roleId":"3a6edacd06b377019827de88f3bdd160","treatmentId":"77bc21b99ea2a67d26e4955b7bc6ce69","doctorInfo":"[{\"id\":\"f907251af90d97e7d89d40cbe1212206\",\"name\":\"测试刘月红\"}]","leadTreatFlag":true}],"approvalFlag":false,"verificationExcessReqList":[],"treatDeptId":"69264e8f851865d91d20f98736176cea","treatDeptName":"无创科","verificationDeptId":"bfb24660a14d9be2f9d2e7a0af7e4b87","verificationDeptName":"皮肤科","verificationUserId":"9d84c6ac6e0d2696ba815c935408417e"}'
        data = data.encode()
        method = 'post'
        response = RunMain().run_main(method=method, url=url, data=data, header=header)
        return response


if __name__ == '__main__':
    Interface().newcustomer()
