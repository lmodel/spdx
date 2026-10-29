package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
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