class ResourceUpdateByPoolsAsyncHandler(BaseAsyncItemHandler, BaseAuthHandler,
                           BaseHandler):
    def _get_controller_class(self):
        return ResourceUpdateByPoolsAsyncController

    async def patch(self, organization_id):
        """
        ---
        description: |
            Modifies an existing resources
            Required permission: INFO_ORGANIZATION
        tags: [resources_update_by_pools]
        summary: Edit resources
        parameters:
        -   name: organization_id
            in: path
            description: id of the organization
            required: true
            type: string
        -   in: body
            name: body
            description: Resources changes
            required: false
            schema:
                type: object
                properties:
                    resource_id:
                        type: array
                        description: list of id's of resources
                    current_pool_id:
                        type: string
                        description: id of current pool
                    target_pool_id:
                        type: string
                        description: id of target pool
        responses:
            200:
                description: Success (returns modified object)
            401:
                description: |
                    Unauthorized:
                    - OE0237: This resource requires authorization
            400:
                description: |
                    Wrong arguments:
                    - OE0211: Parameter is immutable
                    - OE0212: Unexpected parameters
                    - OE0223: Should be an integer
                    - OE0224: Wrong integer argument value
                    - OE0226: Should be True or False
                    - OE0449: Field cannot be changed
                    - OE0537 : Wrong arguments
            403:
                description: |
                    Forbidden:
                    - OE0471: Not enough permissions to migrate to another pool
            404:
                description: |
                    Not found:
                    - OE0002: Pool not found
        security:
        - token: []
        """     
        data = self._request_body()
        user_id = await self.check_self_auth()
        await self.check_permissions('INFO_ORGANIZATION', 'organization', organization_id)
        res = await run_task(self.controller.edit, organization_id, user_id, **data)
        self.write(json.dumps(res, cls=ModelEncoder))
