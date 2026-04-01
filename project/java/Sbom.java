package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A collection of SPDX Elements describing a single package.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sbom extends Bom {

  private List<String> sbomType;

}