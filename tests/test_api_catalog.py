import unittest

from brazil_data_map.api_catalog import build_operation_inventory, validate_operation_inventory


class ApiCatalogTests(unittest.TestCase):
    def test_inventory_includes_read_and_write_operations_with_route_parameters(self) -> None:
        catalog = build_operation_inventory(
            {
                "consulta-api": {
                    "paths": {
                        "/v1/contracts/{id}": {
                            "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}],
                            "get": {"operationId": "readContract", "tags": ["Contracts"]},
                            "delete": {"operationId": "deleteContract", "tags": ["Contracts"]},
                        }
                    }
                }
            }
        )
        self.assertEqual(catalog["operation_count"], 2)
        validate_operation_inventory(catalog)
        get = next(operation for operation in catalog["operations"] if operation["method"] == "GET")
        self.assertEqual(get["parameters"][0]["name"], "id")
        self.assertEqual(get["release_status"], "inventory-only")

    def test_catalog_rejects_duplicate_operations_and_false_completion(self) -> None:
        catalog = build_operation_inventory(
            {"consulta-api": {"paths": {"/v1/reference": {"get": {"operationId": "reference"}}}}}
        )
        invalid = dict(catalog)
        invalid["release_status"] = "complete"
        with self.assertRaisesRegex(ValueError, "must not claim release completion"):
            validate_operation_inventory(invalid)

        invalid = dict(catalog)
        invalid["operations"] = catalog["operations"] * 2
        invalid["operation_count"] = 2
        with self.assertRaisesRegex(ValueError, "duplicate PNCP operation"):
            validate_operation_inventory(invalid)

    def test_ready_read_operation_requires_a_dataset_link(self) -> None:
        catalog = build_operation_inventory(
            {"integration-api": {"paths": {"/v1/modalities": {"get": {"operationId": "listModalities"}}}}}
        )
        operation = catalog["operations"][0]
        operation["release_status"] = "ready"
        with self.assertRaisesRegex(ValueError, "ready operation requires at least one linked table slug"):
            validate_operation_inventory(catalog)

        operation["linked_table_slugs"] = ["pncp-trusted-dom-modalidades"]
        validate_operation_inventory(catalog)


if __name__ == "__main__":
    unittest.main()
