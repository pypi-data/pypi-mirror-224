##
#   Copyright 2021 Alibaba, Inc. and its affiliates. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##

# -*- coding: utf-8 -*-

import re

from dashvector.common.constants import DOC_ID_PATTERN, COLLECTION_AND_PARTITION_NAME_PATTERN
from dashvector.common.handler import RPCRequest
from dashvector.common.types import *
from dashvector.core.proto import dashvector_pb2


class DeleteDocRequest(RPCRequest):

    def __init__(self, *,
                 collection_name: str,
                 ids: IdsType,
                 # filter: Optional[str] = None,
                 partition: Optional[str] = None):
        """
        collection_name: str
        """
        self._collection_name = collection_name

        """
        ids: IdsType
        """
        self._ids = []
        if isinstance(ids, list):
            if len(ids) < 1 or len(ids) > 1024:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest ids list Length({len(ids)}) is Invalid and must be in [1, 1024]")

            for id in ids:
                if isinstance(id, str):
                    if len(id) < 1 or len(id) > 64:
                        raise DashVectorException(
                            code=DashVectorCode.InvalidArgument,
                            reason=f"DashVectorSDK DeleteDocRequest id in ids list Length({len(id)}) is Invalid and must be in [1, 64]")

                    if re.search(DOC_ID_PATTERN, id) is None:
                        raise DashVectorException(
                            code=DashVectorCode.InvalidArgument,
                            reason=f"DashVectorSDK DeleteDocRequest id in ids list Characters({id}) is Invalid and must be in [a-zA-Z0-9] and symbols[_-!@#$%+=.]")
                    self._ids.append(id)
                else:
                    raise DashVectorException(
                        code=DashVectorCode.InvalidArgument,
                        reason=f"DashVectorSDK DeleteDocRequest id in ids list Type({type(id)}) is Invalid")
        elif isinstance(ids, str):
            if len(ids) < 1 or len(ids) > 64:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest ids str Length({len(ids)}) is Invalid and must be in [1, 64]")

            if re.search(DOC_ID_PATTERN, ids) is None:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest ids str Characters({ids}) is Invalid and must be in [a-zA-Z0-9] and symbols[_-!@#$%+=.]")

            self._ids.append(ids)
        else:
            raise DashVectorException(
                code=DashVectorCode.InvalidArgument,
                reason=f"DashVectorSDK DeleteDocRequest ids Type({type(ids)}) is Invalid")

        """
        partition: Optional[str]
        """
        self._partition = None
        if partition is not None:
            if not isinstance(partition, str):
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest partition Type({type(partition)}) is Invalid")

            if len(partition) < 3 or len(partition) > 32:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest partition Length({len(partition)}) is Invalid and must be in [3, 32]")

            if re.search(
                    COLLECTION_AND_PARTITION_NAME_PATTERN,
                    partition) is None:
                raise DashVectorException(
                    code=DashVectorCode.InvalidArgument,
                    reason=f"DashVectorSDK DeleteDocRequest partition Characters({partition}) is Invalid and must be in [a-zA-Z0-9] and symbols[_, -]")

            self._partition = partition

        """
        DeleteDocRequest: google.protobuf.Message
        """
        delete_request = dashvector_pb2.DeleteDocRequest()
        delete_request.ids.extend(self._ids)
        if self._partition is not None:
            delete_request.partition = self._partition

        super().__init__(request=delete_request)

    @property
    def collection_name(self):
        return self._collection_name
